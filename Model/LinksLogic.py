import csv
import Model.Link


class LinksLogic:

    _links = []

    def read_links(self, path: str, item_count: int) -> list:
        with open(path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')

            for row in csv_reader:
                link = Model.Link.Link(row[0], row[1], row[2])
                self._links.append(link.__dict__)

        self._links.pop(0)
        return self._links[0: int(item_count)]
