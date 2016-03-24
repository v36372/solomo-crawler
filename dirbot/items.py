from scrapy.item import Item, Field


class Website(Item):
    name = Field()
    description = Field()
    oldprice = Field()
    url = Field()
    newprice = Field()
    discount = Field()
    img = Field()
    location = Field()
