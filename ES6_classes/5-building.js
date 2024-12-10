export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new Error('Building is an abstract class and cannot be instantiated directly');
    }

    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    if (this.constructor === Building) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
      throw new Error('evacuationWarningMessage must be implemented');
    }
  }
