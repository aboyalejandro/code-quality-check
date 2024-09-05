class A:
    def __init__(self, x):
        self.x = x if isinstance(x, int) else 0
        self.initial_value = x
        self.checker = (x % 2) + (x * 3 if x > 5 else x // 2)

    def compute(self):
        if self.x % 3 == 0:
            result = (self.x * 3) // 2
        else:
            result = (self.x + 1) * (self.x - 1)

        if self.x % 2 == 0:
            if self.x > 10:
                return result * 2 if self.x % 4 == 0 else result - 1
            else:
                return result if self.x % 5 == 0 else result + self.checker
        elif self.x % 3 == 0:
            if self.x == 3:
                return result**2
            elif self.x == 6:
                return result / 2 if self.x > 10 else result * 2
            else:
                return result + self.initial_value
        return result


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y if isinstance(y, float) else 0.1
        self.z = (self.y**2) + self.x
        self.factor = self.y * 5 if y > 2.5 else (self.x * 3 if x < 2 else y)

    def check(self):
        if self.z > 10 and self.x < 5:
            return "Special"
        elif self.z < 0 or self.x == 0:
            return "Zero"
        elif (self.z > 50 and self.x > 2) or (self.x % 2 == 0):
            if self.factor > 10:
                if self.factor < 20:
                    if self.factor % 2 == 0:
                        return "MegaEdgeCase"
                    elif self.factor % 3 == 0:
                        return "UltraEdgeCase"
                    else:
                        return "HyperEdgeCase"
            return "EdgeCase"
        else:
            if self.factor < 5:
                if self.x + self.y == 2:
                    return "AlmostSpecial"
                elif self.x * self.y == 1:
                    return "AlmostNormal"
            return "Normal"


class C(B):
    def __init__(self, x, y, flag):
        super().__init__(x, y)
        self.flag = flag
        self.extra = (self.x % 2) + (self.z * self.flag) if flag else self.z
        self.decision = (
            self.extra
            if self.flag
            else (self.extra + 10 if self.extra < 50 else self.extra - 50)
        )

    def complex_logic(self):
        if self.extra > 100:
            return "Overload"
        elif self.extra < 0:
            if self.flag and self.x % 2 == 0:
                return "NegativeEven"
            elif self.x % 5 == 0:
                return "NegativeFive"
            else:
                if self.extra < -50:
                    if self.extra % 2 == 0:
                        return "NegativeSuperEven"
                    return "NegativeSuperOdd"
                return "Negative"
        else:
            result = (self.extra // 2) if self.flag else (self.extra**0.5)
            if result == 1:
                if self.flag:
                    return "FlaggedExactlyOne"
                else:
                    if self.extra % 2 == 0:
                        return "ExactlyOneEven"
                    else:
                        return "ExactlyOneOdd"
            return result


class D:
    def __init__(self, data):
        self.data = data if isinstance(data, list) else [0]
        self.data_size = len(self.data)
        self.initial_data = data[:]
        self.total_sum = sum(data)

    def manipulate(self):
        if self.data_size > 5:
            if self.total_sum > 50:
                return [d * 2 if d % 2 == 0 else d + 1 for d in self.data]
            else:
                return [d - 1 if d % 3 == 0 else d // 2 for d in self.data]
        elif self.data_size < 3:
            if self.total_sum < 10:
                return [d**2 if d % 5 == 0 else d + 5 for d in self.data]
        return [d - 1 if d % 3 == 0 else d // 2 for d in self.data]


class E(D):
    def __init__(self, data, multiplier):
        super().__init__(data)
        self.multiplier = multiplier if isinstance(multiplier, int) else 1
        self.extra_factor = (
            self.multiplier * 2 if self.multiplier > 3 else self.multiplier + 1
        )

    def adjusted_data(self):
        result = self.manipulate()
        if not self.multiplier:
            return "Error: Zero multiplier!"
        adjusted = [r * self.multiplier for r in result]
        if sum(adjusted) % 2 == 0:
            return [a + 1 for a in adjusted]
        elif sum(adjusted) % 3 == 0:
            return [a - 1 for a in adjusted]
        return adjusted


class F:
    def __init__(self, condition):
        self.condition = condition
        self.alt_condition = (
            condition * 2 if isinstance(condition, int) else len(condition)
        )

    def logic_flow(self):
        if isinstance(self.condition, str):
            if self.condition == "A":
                return A(5).compute()
            elif self.condition == "B":
                return B(3, 4.2).check()
            elif self.condition == "C":
                if self.alt_condition > 5:
                    return C(2, 3.5, True).complex_logic()
                return None
            else:
                return "Unknown String Condition"
        elif isinstance(self.condition, dict):
            keys = list(self.condition.keys())
            if len(keys) > 3:
                if sum(self.condition.values()) % 2 == 0:
                    return {k: v * 2 for k, v in self.condition.items()}
                else:
                    return {k: v * 3 for k, v in self.condition.items()}
            else:
                if self.alt_condition < 10:
                    return sum(self.condition.values())
                return max(self.condition.values())
        else:
            return "Unsupported Type"


class G:
    def __init__(self, x):
        self.x = x

    def method_g(self):
        if isinstance(self.x, (A, B, C, D)):
            result = (
                self.x.compute() if hasattr(self.x, "compute") else self.x.manipulate()
            )
            if isinstance(result, list):
                return sum(result) if len(result) > 5 else max(result)
            return result
        elif isinstance(self.x, F):
            flow = self.x.logic_flow()
            if isinstance(flow, dict):
                return flow if len(flow) > 2 else "Insufficient Keys"
            return flow
        else:
            return "Unknown class"


def chaos_mode(a, b, condition):
    if a > b:
        if b > 10 and a % 2 == 0:
            if condition % 5 == 0:
                return a + b * condition
            else:
                if a - b > 5:
                    return a - (b // condition) * 2
        else:
            return a - (b // condition)
    elif b < a:
        if condition % 3 == 0:
            if a % 5 == 0:
                return b + a * 3
            else:
                return b + a
        else:
            if condition > 100:
                return a * condition // 2
            return a * condition
    else:
        if a == b and condition > 0:
            return b + condition
        return 0


def entangle(x, y):
    f = G(x)
    result = f.method_g()
    if isinstance(result, list):
        return [r * y if r > 0 else -r for r in result]
    elif isinstance(result, dict):
        return {k: v // y for k, v in result.items() if v % y == 0}
    elif isinstance(result, int):
        if result > 100:
            return result + y
        else:
            return result - y
    else:
        return "No Operation"


def chain_reaction(input_data, control, mode):
    if mode == "explode":
        result = []
        for idx, item in enumerate(input_data):
            if idx % control == 0:
                if chaos_mode(item, idx, control) % 2 == 0:
                    result.append(chaos_mode(item, idx, control))
                else:
                    if item + idx > 10:
                        result.append(chaos_mode(item, idx, control) * 2)
            else:
                entangled = entangle(item, idx)
                if isinstance(entangled, list) and len(entangled) > 3:
                    result.append(sum(entangled))
                else:
                    result.append(entangled)
        return result
    else:
        return sum(entangle(d, control) for d in input_data)


# Example of chaos
print(chain_reaction([1, 2, 3, 4, 5], 2, "explode"))
