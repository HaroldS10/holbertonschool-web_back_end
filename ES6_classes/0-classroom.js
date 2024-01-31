export default class ClassRoom {
  constructor(maxStudentsSize) {
    this.maxStudentsSize = maxStudentsSize;
  }

  set maxStudentsSize(value) {
    this._maxStudentsSize = value;
  }

  get maxStudentsSize() {
    return this._maxStudentsSize;
  }
}
