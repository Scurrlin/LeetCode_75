class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        list = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = [ p for p in products if len(p) > i and p[i] == c ]
            list.append(products[:3])
        return list