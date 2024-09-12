from toolz import compose, partial
from operator import gt


class Match:
    def __init__(self, value, matched=False, result=None):
        self.value = value
        self.matched = matched
        self.result = result

    def when(self, condition, result):
        if self.matched:
            return self
        is_match = condition(self.value)
        return Match(
            value=self.value,
            matched=is_match,
            result=result if is_match else None
        )

    def orElse(self, default):
        return self.result if self.matched else default


# res = (
#     Match("2asd")
#         .when(lambda x: len(x) < 2, "first")
#         .when(compose(partial(gt, 5), len), "second")
#         .when(str.isdigit, "digit")
#         .orElse("nothing")
# )