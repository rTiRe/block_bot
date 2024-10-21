from aiogram import Router

from .profile.router import router as profile_router

router = Router()
router.include_router(profile_router)
