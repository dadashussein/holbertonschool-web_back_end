/* eslint-disable import/extensions */
/* eslint-disable jest/prefer-expect-assertions */
/* eslint-disable jest/no-test-return-statement */
import handleResponseFromAPI from './2-then.js';

describe('handleResponseFromAPI', () => {
  it('should resolve with a successful response', () => {
    const promise = Promise.resolve();
    return handleResponseFromAPI(promise).then((response) => {
      expect(response).toStrictEqual({ status: 200, body: 'success' });
    });
  });

  it('should reject with an error', () => {
    const promise = Promise.reject();
    return handleResponseFromAPI(promise).catch((error) => {
      expect(error).toBeInstanceOf(Error);
    });
  });
});
