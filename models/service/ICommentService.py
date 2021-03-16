from models.service.implements.CommentImpl import CommentImpl
from models.service.ITargetService import ITargetService

class ICommentService :
    def hateComment(bot, username, message) :
        target = ITargetService.getUserIdFromUsername(bot, username)
        return CommentImpl.hateComment(bot, target, message)