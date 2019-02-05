import React from "react";

export default class PhotoSlider extends React.PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      currentIndex: 0
    };
    this.getNextIndex = this.getNextIndex.bind(this);
    this.getPreviousIndex = this.getPreviousIndex.bind(this);
  }
  getNextIndex() {
    return (this.state.index + 1) % this.props.photos.length;
  }

  getPreviousIndex() {
    return this.state.index > 0 ? this.state.index - 1 : this.props.photos.length - 1;
  }
  render() {
    return null;
  }
}
