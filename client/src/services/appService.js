import faker from "faker";
import axios from "axios";
import Axios from "axios";

export default class xService {
  getSimilarPeople(_photo, _databaseId) {
    return new Promise((resolve, reject) => {
      setTimeout(
        () =>
          resolve(
            new Array(10).fill(null).map(el => ({
              name: faker.fake(
                "{{name.lastName}}, {{name.firstName}}"
              ),
              photo: faker.image.avatar(),
              ratio: faker.finance.amount(0, 1, 2)
            }))
          ),
        // reject("xd"),
        100
      );
    });
  }

  getAllResults() {
    return axios({
      method: 'get',
      url: 'http://localhost:5000/recentMatches'
    }).then(response => response.data)
  }

  getDataBases() {
    return new Promise(resolve => {
      setTimeout(
        () =>
          resolve(
            new Array(3).fill(null).map((_, i) => ({
              id: i,
              name: faker.name.firstName(),
              description: faker.lorem.paragraph(3),
              photos: new Array(18).fill(null).map(() => faker.image.avatar()),
            }))
          ),
        100
      );
    });
  }
}
