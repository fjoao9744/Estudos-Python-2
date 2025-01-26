from dataclasses import make_dataclass, field

Estoque = make_dataclass(
    "estoque",
    [("items", list, field(default_factory=list))],
    namespace={"add":lambda self, x: self.items.append(x)}
)

stock = Estoque()
stock.add("smogon")
stock.add("smogon")
stock.add("smogon")

print(stock)


