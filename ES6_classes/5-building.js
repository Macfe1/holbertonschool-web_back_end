export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }

    this._sqft = sqft;

    if (new.target === Building) {
      console.error('Building is an abstract class and cannot be instantiated directly');
    }

    if (this.constructor !== Building
        && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  static evacuationWarningMessage() {
    throw new Error('ErClass extending Building must override evacuationWarningMessage');
  }
}
