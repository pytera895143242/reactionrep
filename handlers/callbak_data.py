import random
import asyncio


akk1 = 0
akk2 = 0
akk3 = 0
akk4 = 0
akk5 = 0
akk6 = 0
akk7 = 0
akk8 = 0
akk9 = 0
akk10 = 0
akk11 = 0
akk12 = 0
akk13 = 0
akk14 = 0
akk15 = 0
akk16 = 0
akk17 = 0

async def akkaut1(): #+79867995615
    from pyrogram import Client,idle,handlers
    app1 = Client('session1', 15429738, 'c147b713a6e1e7cbcdc0f92565605945')
    await app1.start()
    return app1

async def akkaut2(): #79867996353
    from pyrogram import Client,idle,handlers
    app2 = Client('session2', 17863610, '29204188291a4e719ffcb2f47a64465c')
    await app2.start()
    return app2

# def akkaut3(): # +79228215828
#     from pyrogram import Client,idle,handlers
#     app3 = Client('session3', 12663241, '46c99cb112f8c8942bc6b3e3eb9ce0d1')
#     app3.start()
#     return app3

async def akkaut4(): #+79228216535
    from pyrogram import Client,idle,handlers
    app4 = Client('session4', 13164973, 'eb273111bceeb88b4a86804de21ebf68')
    await app4.start()
    return app4

async def akkaut5(): #+79228215677
    from pyrogram import Client,idle,handlers
    app5 = Client('session5', 19033993, 'b0113f5c4c807f47a39583e1c940c2e9')
    await app5.start()
    return app5

async def akkaut6(): #+79228215833
    from pyrogram import Client,idle,handlers
    app6 = Client('session6', 15324017, 'cab7928a596f34a201f229070abe252f')
    await app6.start()
    return app6

async def akkaut7(): #+79228215700
    from pyrogram import Client,idle,handlers
    app7 = Client('session7', 19770891, '298e60af1f84fba0a79868dcc3d6d542')
    await app7.start()
    return app7

async def akkaut8(): #+79325445644
    from pyrogram import Client,idle,handlers
    app8 = Client('session8', 17214899, 'a1129178e89e49eaaa2c99ae0f11debf')
    await app8.start()
    return app8

async def akkaut9(): #+79325443960
    from pyrogram import Client,idle,handlers
    app9 = Client('session9', 11971822, '657ee3f2eb59eff0d0095324c5d1bb34')
    await app9.start()
    return app9

async def akkaut10(): #+79328610075
    from pyrogram import Client,idle,handlers
    app10 = Client('session10', 15030107, '128417e785ff07dee773827f01e5e319')
    await app10.start()
    return app10

async def akkaut11(): #+79328529294
    from pyrogram import Client,idle,handlers
    app11 = Client('session11', 10053853, 'fd4a45d627e940a11d8d1b6077833ccf')
    await app11.start()
    return app11

async def akkaut12(): #+79328650388
    from pyrogram import Client,idle,handlers
    app12 = Client('session12', 16900797, 'a801fa6c8169859d99989dc100fddbfe')
    await app12.start()
    return app12

async def akkaut13(): #+79228215920
    from pyrogram import Client,idle,handlers
    app13 = Client('session13', 11364559, '7ea5620e981d93ba766d89df316e9e32')
    await app13.start()
    return app13

async def akkaut14(): #+79328622646
    from pyrogram import Client,idle,handlers
    app14 = Client('session14', 14369126, 'f2ba7b20cde3f0313ed3d6abd0c28160')
    await app14.start()
    return app14

async def akkaut15(): # +79228215770
    from pyrogram import Client,idle,handlers
    app15 = Client('session15', 18188269, 'd6d8c42f800e2f45ca3b297f8ef6d83b')
    await app15.start()
    return app15

async def akkaut16(): # +79228216313
    from pyrogram import Client,idle,handlers
    app16 = Client('session16', 13014654, '6086819e51966f88a27357fd07a41391')
    await app16.start()
    return app16

async def akkaut17(): # +79228215898
    from pyrogram import Client,idle,handlers
    app17 = Client('session17', 11149116, 'c60979a4c2c6e82d1fabdb981e941085')
    await app17.start()
    return app17



async def akkaunts(user,id):
    global akk1,akk2,akk3,akk4,akk5,akk6,akk7,akk8,akk9,akk10,akk11,akk12,akk13,akk14,akk15,akk16,akk17
    id = int(id)
    if akk1 == 0:
        akk1 = await akkaut1()
    if akk2 == 0:
        akk2 = await akkaut2()
    # if akk3 == 0:
    #     akk3 = akkaut3()
    if akk4 == 0:
        akk4 = await akkaut4()
    if akk5 == 0:
        akk5 = await akkaut5()
    if akk6 == 0:
        akk6 = await akkaut6()
    if akk7 == 0:
        akk7 = await akkaut7()
    if akk8 == 0:
        akk8 = await akkaut8() # 8 аккаунт еще не запущен !!!!!!!
    if akk9 == 0:
        akk9 = await akkaut9()
    if akk10 == 0:
        akk10 = await akkaut10()
    if akk11 == 0:
        akk11 = await akkaut11()
    if akk12 == 0:
        akk12 = await akkaut12()
    if akk13 == 0:
        akk13 = await akkaut13()
    if akk14 == 0:
        akk14 = await akkaut14()
    if akk15 == 0:
        akk15 = await akkaut15()
    if akk16 == 0:
        akk16 = await akkaut16()
    if akk17 == 0:
        akk17 = await akkaut17()

    await akk1.send_reaction(user, id , "👍")
    await akk2.send_reaction(user, id , "👍")
    await akk4.send_reaction(user, id , "👍")
    await akk5.send_reaction(user, id , "👍")
    await akk6.send_reaction(user, id , "👍")
    await akk7.send_reaction(user, id , "👍")
    await akk8.send_reaction(user, id , "👍")
    await akk9.send_reaction(user, id , "👍")
    await akk10.send_reaction(user, id , "👍")
    await akk11.send_reaction(user, id , "👍")
    await akk12.send_reaction(user, id , "👍")
    await akk13.send_reaction(user, id , "👍")
    await akk14.send_reaction(user, id , "👍")
    await akk15.send_reaction(user, id , "👍")
    await akk16.send_reaction(user, id , "👍")
    await akk17.send_reaction(user, id , "👍")
