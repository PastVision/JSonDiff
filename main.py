import os
import json
from deepdiff import DeepDiff


class JSonDiff:
    def __init__(self, path1, path2) -> None:
        self.path1 = path1
        self.path2 = path2

    def compare(self) -> None:
        total_count = 0
        for f in os.listdir(self.path1):
            if not f.endswith(".json"):
                continue
            json1: dict = json.load(open(os.path.join(self.path1, f), 'rt'))
            json2: dict = json.load(open(os.path.join(self.path2, f), 'rt'))
            result = DeepDiff(json1, json2)['values_changed']
            count = len(result)
            if count == 0:
                print(f'No difference in {f}.')
                return
            diffpath = os.path.join(self.path1, 'diff')
            if not os.path.exists(diffpath):
                os.mkdir(diffpath)
            with open(os.path.join(diffpath, f), 'wt+') as fp:
                fp.write(json.dumps(result, indent=4))
                print(
                    f'{count} differences in {f} saved to {os.path.join(diffpath, f)}')
            total_count += count
        print(f'\nTotal Differences: {total_count}')


if __name__ == '__main__':
    diff = JSonDiff(input('Old Files Path >> '), input('New Files Path >> '))
    diff.compare()
