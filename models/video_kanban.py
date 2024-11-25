from odoo import models, fields, api
from odoo.addons.web_editor.tools import get_video_embed_code

class VideoKanban(models.Model):
    _name = 'video.kanban'
    _description = 'Video Kanban'

    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
    ]

    name = fields.Char(translate=True, index=True, required=True)
    video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your product.')
    embed_code = fields.Html(compute="_compute_embed_code", sanitize=False)

    @api.depends('video_url')
    def _compute_embed_code(self):
        for image in self:
            image.embed_code = get_video_embed_code(image.video_url) or False