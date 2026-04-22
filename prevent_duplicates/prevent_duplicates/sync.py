import frappe
from frappe.model.document import Document
from prevent_duplicates.prevent_duplicates.doctype import DeduplicationIndex


def before_save(doc: Document) -> None:
    index_doc: DeduplicationIndex = frappe.get_doc("DeduplicationIndex", doc.doctype) # type: ignore
    changes = [doc.has_value_changed(f) for f in index_doc.id_fields]
    if not any(changes):
        return
    if not doc.is_new():
        assert doc.name is not None
        index_doc.remove_from_lsh(doc.name) 
    index_doc.insert_into_lsh(doc)

def on_trash(doc: Document) -> None:
    index_doc: DeduplicationIndex = frappe.get_doc("DeduplicationIndex", doc.doctype) # type: ignore
    assert doc.name is not None
    index_doc.remove_from_lsh(doc.name)