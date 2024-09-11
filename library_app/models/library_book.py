from odoo import fields, models
from odoo.exceptions import ValidationError


class Book(models.Model):
    """
    Describe a book catalogue.
    """
    _name = "library.book"
    _describe = "Book"

    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default="True")
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string="Publisher")
    author_ids = fields.Many2many("res.partner", string="Authors")

