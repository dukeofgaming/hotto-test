/*
    Mocking fetch globally due to an issue with watch mode where fetch is not defined.
    If globals are defined in jest.config.js, then the following code is not needed for a regular run, but it still will not work with watch mode. See: https://stackoverflow.com/questions/74945569/cannot-access-built-in-node-js-fetch-function-from-jest-tests
    Some solutions attempted:
    - Adding `fetch: global.fetch` to globals in jest.config.js. But this only works when not using `jest --watch`, which breaks the ability to do TDD.
    - Using MSW's jest-fixed-jsdom environment (https://testing-library.com/docs/react-testing-library/example-intro/#full-example), but this causes other issues, such as this: https://github.com/mswjs/msw/discussions/1919. So, to avoid adding a dependency, this solution was not pursued.
    - Another potential solution was to use node-fetch: https://github.com/node-fetch/node-fetch. However, trying to use this will result in the error where 'import' cannot be used inside a module.
    TODO: Figure out if the mock function below should return a promise or not.
*/

global.fetch = jest.fn(() =>
    Promise.resolve({
        ok          : false,
        status      : 501,
        statusText  : 'Not Implemented',
        json        : () => Promise.resolve({}),
    })
);
