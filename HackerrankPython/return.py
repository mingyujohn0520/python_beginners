class TestYield:
    def gen_iterator(self):
        result_list = []
        for j in range(3):
            print(f"gen_iterator-{j}")
            result_list.append(j)
        return result_list

    def call_gen_iterator(self):
        result_list = self.gen_iterator()
        for i in result_list:
            print(f"call_gen_iterator-{i}")

if __name__ == "__main__":
    obj = TestYield()
    obj.call_gen_iterator()