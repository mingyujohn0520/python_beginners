class TestYield:
    def gen_iterator(self):
        for j in range(3):
            print(f"do_something-{j}")
            yield j

    def call_gen_iterator(self):
        result_list = self.gen_iterator()
        for i in result_list:
            print(f"call_gen_iterator-{i}")

if __name__ == "__main__":
    obj = TestYield()
    obj.call_gen_iterator()