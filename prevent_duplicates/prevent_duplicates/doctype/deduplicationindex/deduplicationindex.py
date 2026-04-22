# Copyright (c) 2026, iron3oxide and contributors
# For license information, please see license.txt

from typing import List, Any

import frappe
import pickle
from datasketch import MinHash, LeanMinHash, MinHashLSH
from frappe.model.document import Document
from prevent_duplicates.prevent_duplicates.storage import get_redis_connection


class DeduplicationIndex(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from prevent_duplicates.prevent_duplicates.doctype.deduplicationindexdocfield.deduplicationindexdocfield import DeduplicationIndexDocField

		doctype_fields: DF.Table[DeduplicationIndexDocField]
		index_doctype: DF.Link
		index_hex: DF.LongText | None
		num_perm: DF.Int
		similarity_threshold: DF.Float
	# end: auto-generated types

	def insert_into_lsh(self, doc: Document) -> None:
		assert doc.name is not None
		minhash = self._generate_minhash(doc)
		lsh = self._get_lsh()
		lsh.insert(doc.name.encode(), minhash)
		self._store_lsh(lsh)

	def remove_from_lsh(self, doc_name: str) -> None:
		lsh = self._get_lsh()
		lsh.remove(doc_name.encode())
		self._store_lsh(lsh)

	def get_names_of_similar_docs(self, doc: Document) -> List[str]:
		minhash = self._generate_minhash(doc)
		lsh = self._get_lsh()
		result = [key for key in lsh.query(minhash) if isinstance(key, bytes)]
		return [key.decode() for key in result]

	def flush_lsh(self) -> None:
		self.index_hex = None
		self.save()
		self.reload()
		assert self.index_hex is None

	@property
	def id_fields(self) -> List[str]:
		return [f.field_name for f in self.doctype_fields if f.is_relevant]

	def _get_lsh(self) -> MinHashLSH:
		if self.index_hex is None:
			redis_conn = get_redis_connection()
			return MinHashLSH(
				num_perm=self.num_perm,
				threshold=self.similarity_threshold,
				storage_config={
					"type": "redis",
					"basename": b"minhash_lsh",
					"redis": {
						"host": redis_conn.host,
						"port": redis_conn.port
						},
				}
			)
		
		lsh: MinHashLSH = pickle.loads(bytes.fromhex(self.index_hex))
		if lsh.is_empty():
			lsh = self._rebuild_lsh(lsh)

		return lsh
	
	def _rebuild_lsh(self, lsh: MinHashLSH) -> MinHashLSH:
		existing_records = frappe.get_all(self.index_doctype)
		for record in existing_records:
			minhash = self._generate_minhash(record["name"])
			lsh.insert(record["name"].encode(), minhash)
		return lsh
	
	def _store_lsh(self, lsh: MinHashLSH) -> None:
		self.index_hex = pickle.dumps(lsh).hex()
		self.save()

	def _get_identifiers(self, doc: Document) -> List[Any]:
		identifiers = doc.get(self.id_fields)
		assert isinstance(identifiers, list)
		return identifiers

	def _generate_minhash(self, doc: Document) -> LeanMinHash:
		minhash = MinHash(num_perm=self.num_perm)
		identifiers = self._get_identifiers(doc)
		for item in identifiers:
			minhash.update(item.encode())
		return LeanMinHash(minhash)