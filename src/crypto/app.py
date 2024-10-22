# from aiohttp import web

# from aiocryptopay import AioCryptoPay, Networks
# from aiocryptopay.models.update import Update

# from src.config.settings import settings


# web_app = web.Application()
# crypto = AioCryptoPay(token=settings.CRYPTO_PAY_TOKEN, network=Networks.TEST_NET)




# async def create_invoice(app) -> None:
#     invoice = await crypto.create_invoice(asset='TON', amount=1.5)
#     print(invoice.bot_invoice_url)



# web_app.add_routes([web.post(settings.CRYPTO_WEBHOOK_URL, crypto.get_updates)])
# web_app.on_shutdown.append(close_session)
# web.run_app(app=web_app, host='localhost', port=3001)