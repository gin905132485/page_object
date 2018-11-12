import csv


class Data:

    def get_data(self, fl_name):

        fl = open(fl_name)
        content = csv.reader(fl)
        data_lst = [i for i in content]
        fl.close()
        return data_lst


    def _login_data(self):

        data = self.get_data("./data/login.csv")
        login_lst = []
        for i,j in enumerate(data):
            if i != 0:
                login_lst.append(j[2:4])
        return login_lst

if __name__ == "__main__":
    d = Data()
    d._login_data()
