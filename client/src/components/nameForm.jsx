import React from "react";

export default class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    this.props.onNameSubmit(this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <>
        <div className="form-title">Let's Be Friends</div>
        <form onSubmit={this.handleSubmit}>
          <input
            type="text"
            placeholder="Your name is..."
            value={this.state.value}
            onChange={this.handleChange}
          />
          <div>
            <input type="submit" value="Next Section" />
          </div>
        </form>
      </>
    );
  }
}
