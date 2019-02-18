import React from "react";
import "./photoSlider.scss";
export default class PhotoSlider extends React.PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      currentIndex: 0,
      photos: this.props.similarPeople.map(item => item.photo),
      move: false,
      moveDirection: ""
    };
    this.getNextIndex = this.getNextIndex.bind(this);
    this.getPreviousIndex = this.getPreviousIndex.bind(this);
    this.handleLeftClick = this.handleLeftClick.bind(this);
    this.handleRightClick = this.handleRightClick.bind(this);
  }
  getNextIndex(step = 1) {
    return (this.state.currentIndex + step) % this.state.photos.length;
  }

  getPreviousIndex(step = 1) {
    return this.state.currentIndex - step >= 0
      ? this.state.currentIndex - step
      : this.state.photos.length + (this.state.currentIndex - step);
  }
  handleLeftClick() {
    this.setState({ move: true, moveDirection: "right" }); // currentIndex: this.getPreviousIndex()
    setTimeout(() => {
      this.setState({
        move: false,
        moveDirection: "",
        currentIndex: this.getPreviousIndex()
      });
    }, 500);
  }
  handleRightClick() {
    this.setState({ move: true, moveDirection: "left" }); // currentIndex: this.getPreviousIndex()
    setTimeout(() => {
      this.setState({
        move: false,
        moveDirection: "",
        currentIndex: this.getNextIndex()
      });
    }, 500);
  }
  render() {
    console.log(this.props);
    const styles = [
      {
        backgroundImage: `url(${this.state.photos[this.getPreviousIndex(2)]})`
      },
      { backgroundImage: `url(${this.state.photos[this.getPreviousIndex()]})` },
      { backgroundImage: `url(${this.state.photos[this.state.currentIndex]})` },
      { backgroundImage: `url(${this.state.photos[this.getNextIndex()]})` },
      { backgroundImage: `url(${this.state.photos[this.getNextIndex(2)]})` }
    ];
    if (this.state.moveDirection == "left") {
      return (
        <div className="photo-slider">
          <div className={"photo static quaternary left"} style={styles[0]} />
          <div
            className={"photo tertiary left"}
            style={styles[1]}
            onClick={this.handleLeftClick}
          />
          <div className={"photo secondary left"} style={styles[2]} />
          <div
            className={"photo primary"}
            style={styles[3]}
            onClick={this.handleRightClick}
          />
          <div className={"photo secondary right"} style={styles[4]} />
        </div>
      );
    }
    if (this.state.moveDirection == "right") {
      return (
        <div className="photo-slider">
          <div className={"photo secondary left"} style={styles[0]} />
          <div
            className={"photo primary"}
            style={styles[1]}
            onClick={this.handleLeftClick}
          />
          <div className={"photo secondary right"} style={styles[2]} />
          <div
            className={"photo tertiary right"}
            style={styles[3]}
            onClick={this.handleRightClick}
          />
          <div className={"photo static quaternary right"} style={styles[4]} />
        </div>
      );
    }
    return (
      <div className="photo-slider">
        <div className={`photo static tertiary left`} style={styles[0]} />
        <div
          className={`photo static secondary left`}
          style={styles[1]}
          onClick={this.handleLeftClick}
        />
        <div className={`photo static primary`} style={styles[2]} />
        <div
          className={`photo static secondary right`}
          style={styles[3]}
          onClick={this.handleRightClick}
        />
        <div className={"static photo quaternary right"} style={styles[4]} />
        <div className="who">{`remainds me of ${this.props.similarPeople[this.state.currentIndex].name} in ${this.props.similarPeople[this.state.currentIndex].ratio * 100} %`}</div>
      </div>
    );
  }
}
