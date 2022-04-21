class MyDict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)


phrases = dict(a="ля-ля",
               b="три рубля",
               c="модница-сковородница",
               d="ёлки-палки",
               e="трезубец посейдона",
               f="дворец уважения",
               g="трикотажный калейдоскоп")

my_dict = MyDict(phrases)
print(my_dict.get("c"))
print(my_dict.get("z"))

# зачёт!
