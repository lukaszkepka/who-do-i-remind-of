import React from "react";

export default class ResultSlider extends React.Component {
  constructor(props) {
    super(props);
    this.state = { index: 0 };
  }
  render() {
    console.log(this.props);
    return (
      <div className="flex">
        <input
          className="no-margin"
          type="button"
          value="<"
          onClick={() =>
            this.setState({
              index:
                this.state.index === 0
                  ? this.props.results.length - 1
                  : this.state.index - 1
            })
          }
        />
        <div className="flex vertical">
          <img
            height="200"
            width="200"
            src={this.props.results[this.state.index].photo}
          />
          <p>{this.props.results[this.state.index].name}</p>
          <p>
            {`Similarity ratio: ${(this.props.results[this.state.index].ratio *
              100).toFixed()}%`}
          </p>
        </div>
        <input
          className="no-margin"
          type="button"
          value=">"
          onClick={() =>
            this.setState({
              index: (this.state.index + 1) % this.props.results.length
            })
          }
        />
      </div>
    );
  }
}
