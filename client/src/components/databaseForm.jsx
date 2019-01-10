import React from "react";

export default class DataBaseForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: null };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
      // TODO hardcoded
    this.setState({ value: 1 });
  }

  handleSubmit(event) {
    this.props.onDataBaseSubmit(this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      
      <form onSubmit={this.handleSubmit}>
        Wybierz bazę:
        <input
          type="text"
          placeholder="Name"
          value={this.state.value}
          onChange={this.handleChange}
        />
        <div>
          <input type="submit" value="Submit" />
        </div>
      </form>
    );
  }
}
