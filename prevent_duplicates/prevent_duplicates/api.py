from typing import List

import frappe

from frappe.model.document import Document
from prevent_duplicates.prevent_duplicates.doctype import DeduplicationIndex


@frappe.whitelist()
def get_dt_fieldnames(doctype: str) -> list[str]:
    meta = frappe.get_meta(doctype, cached=False)
    return [f.fieldname for f in meta.fields if f.fieldname is not None]


@frappe.whitelist()
def flush_dedup_index(doctype: str) -> str:
    index_doc: DeduplicationIndex = frappe.get_doc("DeduplicationIndex", doctype) # type: ignore
    try:
        index_doc.flush_lsh()
        return f"DeduplicationIndex of {doctype} flushed successfully."
    except AssertionError as e:
        return str(e)
    

def get_similar_docs[T: Document](doc: T) -> List[T]:
    index_doc: DeduplicationIndex = frappe.get_doc("DeduplicationIndex", doc.doctype) # type: ignore
    names = index_doc.get_names_of_similar_docs(doc)
    return [frappe.get_doc(doc.doctype, name) for name in names]    # type: ignore
