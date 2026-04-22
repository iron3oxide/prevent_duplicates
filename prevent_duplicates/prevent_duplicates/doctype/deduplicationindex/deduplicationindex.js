// Copyright (c) 2026, iron3oxide and contributors
// For license information, please see license.txt

frappe.ui.form.on("DeduplicationIndex", {
	refresh(frm) {

	},
    index_doctype(frm) {
        frappe.call({
            method: "prevent_duplicates.prevent_duplicates.api.get_dt_fieldnames",
            type: "GET",
            args: {
                doctype: frm.doc.index_doctype,
            },
            freeze: true,
            callback: (r) => {
                let fieldnames = r.message;
                fieldnames.forEach((name) => frm.add_child('doctype_fields', {
                    field_name: name,
                    is_relevant: false,
                }));
                frm.refresh_field('doctype_fields');
            },
            error: (r) => {
                console.log("error")
                console.error(r.message)
            },
            always: (r) => {
            }
        })
    },
});

frappe.ui.form.on("DeduplicationIndex", "flush_index", function(frm) {
    frappe.call(
        {
            method: "prevent_duplicates.prevent_duplicates.api.flush_dedup_index",
            type: "GET",
            args: {
                doctype: frm.doc.index_doctype
            },
            freeze: true,
            callback: (r) => {
                console.log(r.message);
            },
            error: (r) => {
                console.log("Encountered error while trying to flush index: ");
                console.error(r.message);
            },
            always: (r) => {}
        }
    );
});
