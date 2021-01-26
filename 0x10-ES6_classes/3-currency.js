export default class Currency {
  constructor(code, name) {
    if (typeof code === 'string' && typeof name === 'string') {
      this._code = code;
      this._name = name;
    } else {
      throw (TypeError('Attributes must be strings'));
    }
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Attributes must be a string');
    }
    this._name = name;
  }

  set code(code) {
    if (typeof code !== 'string') {
      throw TypeError('Attributes must be a string');
    }
    this._code = code;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this._name} (${this.code})`;
  }
}
