{
    "name": "Library Management",
    "summary": "Manage library catalog and book lending.",
    "author": "Oleh Zahor",
    "license": "AGPL-3",
    "website": "https://github.com/PacktPublishing"
               "/Odoo-15-Development-Essentials",
    "version": "15.0.1.0.0",
    "category": "Services/Library",
    "depends": ["base"],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        # "security/library_security.xml",
       
        # "views/book_view.xml",
        "views/library_menu.xml",
        ],
    "application": True,
}