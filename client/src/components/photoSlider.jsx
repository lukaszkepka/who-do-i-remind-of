import React from "react";
import "./photoSlider.scss";
export default class PhotoSlider extends React.PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      currentIndex: 0,
      photos: ["blue", "white", "yellow", "green", "red", "pink", "purple"],
      move: false
    };
    this.getNextIndex = this.getNextIndex.bind(this);
    this.getPreviousIndex = this.getPreviousIndex.bind(this);
    this.handleLeftClick = this.handleLeftClick.bind(this);
    this.handleRightClick = this.handleRightClick.bind(this);
  }
  getNextIndex(step = 1) {
    //state -> props
    return (this.state.currentIndex + step) % this.state.photos.length;
  }

  getPreviousIndex(step = 1) {
    return this.state.currentIndex - step >= 0 ? this.state.currentIndex - step : this.state.photos.length + (this.state.currentIndex - step);
  }
  handleLeftClick() {
    this.setState({move: true});// currentIndex: this.getPreviousIndex()
    setTimeout(() => {
      this.setState({move: false, currentIndex: this.getPreviousIndex()});
    }, 1000)
  }
  handleRightClick() {
    this.setState({move: true});// currentIndex: this.getPreviousIndex()
    setTimeout(() => {
      this.setState({move: false, currentIndex: this.getNextIndex()});
    }, 1000)
  }
  render() {
    const styles = [
      {background: this.state.photos[this.getPreviousIndex(2)]},
      {background: this.state.photos[this.getPreviousIndex()]},
      {background: this.state.photos[this.state.currentIndex]},
      {background: this.state.photos[this.getNextIndex()]},
      {background: this.state.photos[this.getNextIndex(2)]}
    ];
    // return (
    //   <div className="photo-slider">
    //     <div className={`photo tertiary left`} style={styles[0]}></div>
    //     <div className={`photo secondary left`} style={styles[1]} onClick={this.handleLeftClick}></div>
    //     <div className={`photo primary`} style={styles[2]}></div>
    //     <div className={`photo secondary right`} style={styles[3]} onClick={this.handleRightClick}></div>
    //     <div className="photo quaternary right" style={styles[4]}></div>
    //   </div>
    // );
    return (
      <div className="photo-slider">
        <div className={`photo ${this.state.move ? "secondary left" : " static tertiary left"}`} style={styles[0]}></div>
        <div className={`photo ${this.state.move ? "primary" : "static secondary left"}`} style={styles[1]} onClick={this.handleLeftClick}></div>
        <div className={`photo ${this.state.move ? "secondary right" : "static primary"}`} style={styles[2]}></div>
        <div className={`photo ${this.state.move ? "tertiary right" : "static secondary right"}`} style={styles[3]} onClick={this.handleRightClick}></div>
        <div className="static photo quaternary right" style={styles[4]}></div>
      </div>
    );
  }
}
