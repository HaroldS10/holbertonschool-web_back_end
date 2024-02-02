export default class Building {
    constructor(sqft) {
      const ExisteUnaClaseHija = new.target !== Building;
      const noTieneElMethodoEvacuationWarningMessage = typeof this.evacuationWarningMessage === 'undefined';
      if (ExisteUnaClaseHija && noTieneElMethodoEvacuationWarningMessage) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
  
      this.sqft = sqft;
    }
  
    set sqft(value) {
      if (typeof value !== 'number') {
        throw new TypeError('sqft must be a number');
      }
  
      this._sqft = value;
    }
  
    get sqft() {
      return this._sqft;
    }
  }
