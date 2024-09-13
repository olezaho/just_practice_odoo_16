from odoo import fields, models
from odoo.exceptions import ValidationError


class Book(models.Model):
    """
    Describe a book catalogue.
    """

    _name = "library.book"
    _description = "Library Book"
    _order = "date_published desc, name"
    _rec_name = "short_name"

    short_name = fields.Char(
        "Short Title", required=True, default="Empty", index=True
    )
    notes = fields.Text("Internal Notes")
    state = fields.Selection(
        [("draft", "Not Available"), ("available", "Available"), ("lost", "Lost")],
        "State",
        default="draft",
    )
    description = fields.Html("Description", sanitize=True, strip_style=False)
    cover = fields.Binary("Book Cover")
    date_update = fields.Datetime("Last Update")
    pages = fields.Integer("Number of Pages", groups="base.group_user", states={'lost': [('readonly', True)]}, company_dependent=False, help="cos tam")
    reader_ratings = fields.Float("Reader Average Rating", digits=(14, 4))
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default="True")
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string="Publisher")
    author_ids = fields.Many2many("res.partner", string="Authors")

    cost_price = fields.Float("Book Coast", digits='Product Price')

    def name_get(self):
        result = []
        for rec in self:
            rec_name = "%s (%s)" % (rec.name, rec.date_published)
            result.append((rec.id, rec_name))
        return result
