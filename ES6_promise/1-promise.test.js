// eslint-disable-next-line import/extensions
import getFullResponseFromAPI from './1-promise.js';

describe('getFullResponseFromAPI', () => {
  it('should resolve with a successful response when success is true', () => getFullResponseFromAPI(true).then((response) => {
    expect(response).toStrictEqual({
      status: 200,
      body: 'Success',
    });
  }));

  it('should reject with an error when success is false', () => getFullResponseFromAPI(false).catch((error) => {
    expect(error).toStrictEqual(new Error('The fake API is not working currently'));
  }));
});
