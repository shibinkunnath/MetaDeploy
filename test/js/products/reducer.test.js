import reducer from 'products/reducer';

describe('reducer', () => {
  test('returns initial state', () => {
    const expected = [];
    const actual = reducer(undefined, {});

    expect(actual).toEqual(expected);
  });

  test('handles FETCH_PRODUCTS_SUCCEEDED action', () => {
    const product1 = {
      id: 1,
      title: 'Product 1',
      description: 'This is a test product.',
      category: 'salesforce',
    };
    const product2 = {
      id: 2,
      title: 'Product 2',
      description: 'This is another test product.',
      category: 'salesforce',
    };
    const expected = [product2];
    const actual = reducer([product1], {
      type: 'FETCH_PRODUCTS_SUCCEEDED',
      payload: expected,
    });

    expect(actual).toEqual(expected);
  });
});
