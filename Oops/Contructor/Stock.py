class Stock:
    def __init__(self, prices):
        self.prices = prices
        self.spans = []

    def calculate_span(self):
        stack = []  
        n = len(self.prices)

        for i in range(n):
            while stack and self.prices[i] >= self.prices[stack[-1]]:
                stack.pop()

            if stack:
                span = i - stack[-1]
            else:
                span = i + 1

            self.spans.append(span)

            stack.append(i)

    def calculate_cube(self):
        
        result = [span ** 3 if span > 1 else span for span in self.spans]
        return result

    def display_result(self):
        print("Input prices:", self.prices)
        print("Spans:", self.spans)
        print("Cubed spans (if greater than 1):", self.calculate_cube())


prices = [100, 80, 60, 70, 60, 75, 85]
span_calculator = Stock(prices)
span_calculator.calculate_span()
span_calculator.display_result()
