import faker from "faker";

export default class xService {
  getSimilarPeople(_photo) {
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
            //reject("xd"),
        1000
      );
    });
  }

  getAllResults() {
    return new Promise(resolve => {
      setTimeout(
        () =>
          resolve(
            new Array(10).fill(null).map(() => ({
              userName: faker.name.firstName(),
              celebrityPhoto: faker.image.avatar(),
              celebrityName: faker.fake(
                "{{name.lastName}}, {{name.firstName}}"
              ),
              ratio: faker.finance.amount(0, 1, 2)
            }))
          ),
        1000
      );
    });
  }

  getDataBases() {
    return new Promise(resolve => {
      setTimeout(
        () =>
          resolve(
            new Array(3).fill(null).map(() => ({
              name: faker.name.firstName(),
              description: faker.lorem.paragraph(3),
              photos: new Array(10).fill(null).map(() => faker.image.avatar()),
            }))
          ),
        1000
      );
    });
  }
}
