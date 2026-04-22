# Copyright (c) 2026, iron3oxide and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DeduplicationIndexDocField(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		field_name: DF.Data
		is_relevant: DF.Check
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	def autoname(self) -> str:
		return f"{self.parenttype}_{self.field_name}"
