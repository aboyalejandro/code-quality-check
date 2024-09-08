class C(B):
    # ... existing code ...

    def complex_logic(self):
        if self.extra > 100:
            return "Overload"
        elif self.extra < 0:
            return self._handle_negative_extra()
        else:
            return self._handle_positive_extra()

    def _handle_negative_extra(self):
        if self.flag and self.x % 2 == 0:
            return "NegativeEven"
        elif self.x % 5 == 0:
            return "NegativeFive"
        elif self.extra < -50:
            return "NegativeSuperEven" if self.extra % 2 == 0 else "NegativeSuperOdd"
        return "Negative"

    def _handle_positive_extra(self):
        result = (self.extra // 2) if self.flag else (self.extra**0.5)
        if result == 1:
            return self._handle_result_one()
        return result

    def _handle_result_one(self):
        if self.flag:
            return "FlaggedExactlyOne"
        return "ExactlyOneEven" if self.extra % 2 == 0 else "ExactlyOneOdd"
