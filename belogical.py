
from telethon import events

import asyncio

import os

import sys

import random

#Написано и переведено мной, это был оочень тяжёлый труд

@borg.on(events.NewMessage(pattern=r"\.belo", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("`Добро пожаловать в галерею мыслей в 3 часа ночи. by Konori`")

    await asyncio.sleep(2)

    x=(random.randrange(1,97))

    if x==1:

        await event.edit("`\"Пузыри на воде и капли дождя - полная противоположность друг другу.\"`")
    if x==2:

        await event.edit("`\"Когда вы покупаете ластик, вы буквально платите за свои ошибки.\"`")

    if x==3:

        await event.edit("`\"Человек, о котором ты заботишься больше всего, способен причинить боль как никто другой.\"`")

    if x==4:

        await event.edit("`\"Если люди колонизируют Луну, там, вероятно, появятся дома престарелых, поскольку более слабая гравитация позволит пожилым чувствовать себя сильнее.\"`")

    if x==5:

        await event.edit("`\"Любое видео с надписью «Угарный конец>> или <<вы не подозреваете, что случилось в конце» в заголовке, зачастую слишком длинное.\"`")

    if x==6:

        await event.edit("`\"Ваш возраст в годах - это сколько раз ВЫ облетели вокруг Солнца, но ваш возраст в месяцах - это сколько раз Луна облетела ВАС.\"`")

    if x==7:

        await event.edit("`\"Прикусывание языка во время еды - прекрасный пример того, как вы все еще можете облажаться, даже имея многолетний опыт.\"`")

    if x==8:

        await event.edit("`\"Рассказ о том, что ваш дом работает от беспроводного ядерного термоядерного реактора, который находится на расстоянии 150 миллионов километров, звучит гораздо круче, чем просто сказать, что у вас есть солнечные батареи на крыше.\"`")

    if x==9:

        await event.edit("`\"Самое ужасное чувство - когда кто-то улыбается тебе на улице, а ты не успеваешь улыбнуться в ответ..\"`")

    if x==10:

        await event.edit("`\"Зубы постоянно нуждаются в обслуживании, чтобы предотвратить их разрушение при жизни, и все же им удается выжить в течение тысяч лет, похороненными в окаменелостях.\"`")

    if x==11:

        await event.edit("`\"Даже <<Самая Важная Папка>> лежит в дальнем ящике стола.\"`")

    if x==12:

        await event.edit("`\"Иногда проснувшись утром вам кажется, будто вы снова смотрите дерьмовый фильм, который вы решили бросить.\"`")

    if x==13:

        await event.edit("`\"Если сегодня всё пройдет гладко и размеренно, вы даже не вспомните этот день.\"`")

    if x==14:

        await event.edit("`\"Когда вы встречаете новых людей в реальной жизни, вы открываете больше персонажей для своих снов.\"`")

    if x==15:

        await event.edit("`\"Возможно, если бы переименовали солнцезащитный крем в «противораковый крем», больше людей стали бы его носить.\"`")

    if x==16:

        await event.edit("`\"200 лет назад люди никогда бы не подумали, что люди в будущем будут общаться, молча стуча по стеклу.\"`")

    if x==17:

        await event.edit("`\"Родители беспокоятся о том, что СКАЧИВАЮТ их сыновья, и беспокоятся о том, что ЗАГРУЖАЮТ их дочери.\"`")

    if x==18:

        await event.edit("`\"Звучит безумно, но вы можете быть одного возраста с кем-то, но на совершенно разных уровнях развития в жизни.\"`")

    if x==19:

        await event.edit("`\"Когда ты думаешь, что хочешь умереть, ты действительно не хочешь умереть, ты просто не хочешь жить как сейчас.\"`")

    if x==20:

        await event.edit("`\"Технически, ни один человек не был в пустой комнате.\"`")

    if x==21:

        await event.edit("`\"Лук - бас-гитарист среди еды. Возможно, он вам не понравится будучи в одиночку, но вы бы жалели, если бы его вообще не было.\"`")

    if x==22:

        await event.edit("`\"Мы бегаем повсюду в видеоиграх, потому что нам лень ходить, но в реальной жизни мы ходим везде, потому что нам лень бегать.\"`")

    if x==23:

        await event.edit("`\"Каждое принятое вами решение заставляло вас читать это предложение...\"`")

    if x==24:

        await event.edit("`\"Слово <<ТИХО>> зачастую говорится слишком громко.\"`")

    if x==25:

        await event.edit("`\"Все хотят, чтобы вы усердно работали, но никто не хочет слышать о том, как усердно вы работаете.\"`")

    if x==26:

        await event.edit("`\"Мы чистим зубы волосинками на палочке и чистим волосы зубьями на палочке.\"`")

    if x==27:

        await event.edit("`\"Никто не помнит ваши неловкие моменты, ведь все слишком заняты, вспоминая свои собственные.\"`")

    if x==28:

        await event.edit("`\"Глупые люди пытаются произносить простые идеи как можно более сложными, в то время как умные люди пытаются говорить сложные идеи как можно проще.\"`")

    if x==29:

        await event.edit("`\"Некоторые люди думают, что они лучше вас, потому что они СТАЛИ богаче. Некоторые люди думают, что они лучше вас, потому что они РОСЛИ беднее.\"`")

    if x==30:

        await event.edit("`\"Самая большая ирония в том, что компьютеры и мобильные телефоны были изобретены для экономии времени!\"`")

    if x==31:

        await event.edit("`\"После того, как мед был впервые обнаружен, был период, когда люди испытывали вкус любой доступной слизи от насекомых.\"`")

    if x==32:

        await event.edit("`\"Вы поймёте, что стареете, когда родители начинут печалить вас, а не вы их.\"`")

    if x==33:

        await event.edit("`\"Люди созданы для того, чтобы учиться на собственном опыте, но сейчас система образования сама учит нас, поэтому мы не получаем никакого опыта.\"`")

    if x==34:

        await event.edit("`\"Сосредоточившись на мигании, ваш организм перекладывает ответственность за это дело на ваш организм ... То же самое для дыхания...\"`")

    if x==35:

        await event.edit("`\"Водители, которые спешат преодолевать пробки, обычно сами и вызывают аварии, которые создают пробку, которую они так пытались избежать.\"`")

    if x==36:

        await event.edit("`\"Персонажи, которые женятся в художественной литературе, были буквально созданы друг для друга.\"`")

    if x==37:

        await event.edit("`\"Дети - это чистый жесткий диск, который можно запрограммировать на любом языке..\"`")

    if x==38:

        await event.edit("`\"Возможно есть чудодейственное лекарство, которое излечивает человека от всех болезней, о котором мы никогда не узнаем, ведь оно не действует на крыс.\"`")

    if x==39:

        await event.edit("`\"Носороги получили рог для защиты, но именно он и заставляет их вымирать.\"`")

    if x==40:

        await event.edit("`\"Помни: только эта жизнь имеет цену!.\"`")

    if x==41:

        await event.edit("`\"Сон - это пробная версия смерти, она даже идет с рекламой, основанной на вашей активности.\"`")

    if x==42:

        await event.edit("`\"Самая нереальная вещь в шпионских фильмах - насколько же там чистая система вентиляции!\"`")

    if x==43:

        await event.edit("`\"В играх мы играем в простые режимы, чтобы разблокировать сложные. В жизни же мы играем в сложные режимы, чтобы разблокировать простые.\"`")

    if x==44:

        await event.edit("`\"Молчаливые люди кажутся умнее разговорчивых, потому что они держат свои глупые мысли при себе.\"`")

    if x==45:

        await event.edit("`\"Если Гренландия (Greenland) на самом деле станет зеленой - мы все облажались.\"`")

    if x==46:

        await event.edit("`\"Если кто-то говорит умные вещи в вашем сне, это на самом деле показывает ваш собственный интеллект.\"`")

    if x==47:

        await event.edit("`\"Знаменитые цитаты из фильмов зачисляются актеру, а не самому человеку, который их написал.\"`")

    if x==48:

        await event.edit("`\"Никто на самом деле не учит вас, как ездить на велосипеде. Они просто обманывают вас, пока вы сами это не сделаете.\"`")

    if x==49:

        await event.edit("`\"- Мы живём лишь раз. - Нет, мы умираем лишь раз, живём мы каждый день.\"`")

    if x==50:

        await event.edit("`\"Вы, вероятно, уже забыли о 80% всей своей жизни, и большинство воспоминаний, которые вы помните, вовсе не всегда точно соответствуют тому, что произошло на самом деле.\"`")

    if x==51:

        await event.edit("`\"В будущем детям будет намного сложнее побеждать своих родителей в видеоиграх.\"`")

    if x==52:

        await event.edit("`\"У всех есть недостатки, если вы не знаете свои, поздравляю, у вас есть новый.\"`")

    if x==53:

        await event.edit("`\"Воспитание ребенка - это тренировка вашей замены.\"`")

    if x==54:

        await event.edit("`\"Настоящий друг — это человек, который выскажет тебе в глаза все, что о тебе думает, а всем скажет, что ты — замечательный человек.\"`")

    if x==55:

        await event.edit("`\"Всегда есть кто-то, кто ненавидил тебя без всякой на то причины и до сих пор это делает.\"`")

    if x==56:

        await event.edit("`\"После того, как сумели получить попкорн, должно быть много случайных семян были поджарены, чтобы увидеть, будет ли он иметь тот же эффект.\"`")

    if x==57:

        await event.edit("`\"Чем важнее хорошо выспаться ночью, тем труднее заснуть.\"`")

    if x==58:

        await event.edit("`\"Тем, кто могут правильно описать тип стрижки, которую они хотят новому стилисту, заготовлено отдельное место в раю.\"`")

    if x==59:

        await event.edit("`\"Слишком много людей тратят деньги, которые они НЕ ЗАРАБОТАЛИ, чтобы покупать вещи, которые они НЕ ХОТЯТ, чтобы произвести впечатление на людей, которые им НЕ НРАВЯТЯ!\"`")

    if x==60:

        await event.edit("`\"Сотрудники тематического парка должны хорошо понимать разницу между криками ужаса и простым волнением.\"`")

    if x==61:

        await event.edit("`\"С 6 до 6:30 больше звучит как полчаса, чем с 5:50 до 6:20\"`")

    if x==62:

        await event.edit("`\"Правильный ввод пароля прямо при последней попытке входа в систему перед блокировкой - это самое близкое чувство к чувству обезвреживания бомбы в последнюю минуту, которое испытает большинство из нас.\"`")

    if x==63:

        await event.edit("`\"Прослушивание подкастов перед сном - взрослая версия сказки на ночь.\"`")

    if x==64:

        await event.edit("`\"Если бы все преступники прекратили грабить, то индустрия безопасности разорилась, и они могли бы легко вернуться к грабежу.\"`")

    if x==65:

        await event.edit("`\"Тонна китов в действительности выглядит только как половина кита.\"`")

    if x==66:

        await event.edit("`\"Когда вы стареете, то старый вы - технически новый вы, а  молодой вы - старый вы.\"`")

    if x==67:

        await event.edit("`\"Вы, вероятно, не найдете много негативных отзывов о парашютах в Интернете.\"`")

    if x==68:

        await event.edit("`\"Мы показываем больше любви и восхищения людям, когда их нет рядом, чтобы ценить это.\"`")

    if x==69:

        await event.edit("`\"Мы практиковались спать тысячи раз, но до сих пор не можем делать это очень хорошо или быть последовательными.\"`")

    if x==70:

        await event.edit("`\"Люди с большим энтузиазмом относятся к переезду на другую планету с враждебным окружением, чем к сохранению Земли - планеты, для которой они идеально подходят.\"`")

    if x==71:

        await event.edit("`\"Самый счастливый этап жизни большинства людей - это когда их мозг еще не полностью развит..\"`")

    if x==72:

        await event.edit("`\"Самый эффективный будильник - полный пузырь.\"`")

    if x==73:

        await event.edit("`\"Вы, вероятно, синхронизировали моргания с миллионами людей.\"`")

    if x==74:

        await event.edit("`\"Поскольку мы сначала тестируем лекарства на животных, медицина крыс уже должна быть на годы впереди медицины человека.\"`")

    if x==75:

        await event.edit("`\"Ночь перед выходными более приятна, чем сами выходные.\"`")

    if x==76:

        await event.edit("`\"Если у тебя получилось обмануть человека, это не значит, что он дурак, это значит, что тебе доверяли больше, чем ты этого заслуживаешь..\"`")

    if x==77:

        await event.edit("`\"Где-то два лучших друга встречаются впервые.\"`")

    if x==78:

        await event.edit("`\"Наш мозг одновременно ненавидит нас, любит нас, не заботится о нас и управляет каждым нашим движением.\"`")

    if x==79:

        await event.edit("`\"Быть мужчиной - это вопрос рождения. Быть мужчиной - это вопрос возраста. Но быть джентльменом - дело выбора.\"`")

    if x==80:

        await event.edit("`\"Скоро родители будут скрывать свой социальный аккаунт от своих детей, чаще чем дети будут скрывать свои аккаунты от родителей.\"`")

    if x==81:

        await event.edit("`\"Википедия - это то, чем должен был быть Интернет.\"`")

    if x==82:

        await event.edit("`\"Тематический парк - единственное место, где вы можете слышать крики на расстоянии и не беспокоиться.\"`")

    if x==83:

        await event.edit("`\"Беспроводное зарядное устройство для телефона предлагает меньше свободы передвижения, чем проводное.\"`")

    if x==84:

        await event.edit("`\"Если вы неоднократно критикуете кого-то за то, что им нравится то, что вам не нравится, им это вовсе не перестанет нравиться. Им перестанет нравится вы.\"`")

    if x==85:

        await event.edit("`\"Где-то есть бабушка, чей внук действительно <<самый красивый мальчик>> в мире.\"`")

    if x==86:

        await event.edit("`\"Если когда-нибудь телепортация человека станет реальностью, люди все равно будут опаздывать на работу.\"`")

    if x==87:

        await event.edit("`\"Первые люди, которые ели крабов, наверняка были очень голодны, чтобы съесть бронированного морского паука\"`")

    if x==88:

        await event.edit("`\"Делать что-то в одиночку грустно, но делать это самостоятельно круто..\"`")

    if x==89:

        await event.edit("`\"В падающем самолёте нет атеистов.\"`")

    if x==90:

        await event.edit("`\"В вашем плейлисте всегда есть как минимум одна песня, которую вы всегда пропускаете, но никогда не удаляете.\"`")

    if x==91:

        await event.edit("`\"Дети следующего поколения, вероятно, будут ненавидеть нас за то, что мы взяли все хорошие имена пользователей..\"`")

    if x==92:

        await event.edit("`\"Пузыри для рыб, как дождь для человека..\"`")

    if x==93:

        await event.edit("`\"Чем больше людей вы встречаете, тем больше вы понимаете и цените то, как же хорошо ваши родители воспитывали вас.\"`")

    if x==94:

        await event.edit("`\"Победи себя и выиграешь тысячи битв.\"`")

    if x==95:

        await event.edit("`\"Когда-нибудь вы либо не проснетесь, либо не уснете.\"`")     

    if x==96:

        await event.edit("`\"Бермудский треугольник может быть порталом для выхода из этой симуляции.\"`")
    
    if x==97:

        await event.edit("`\"Если поставить солнечные батареи над парковками, наши машины не будут нагреваться, и у нас будет много чистой энергии..\"`")

    
