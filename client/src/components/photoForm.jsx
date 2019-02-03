import React from "react";

export default class PhotoForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { selectedFile: null, fileUrl: "" };

    this.handleFileChanged = this.handleFileChanged.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleFileChanged(event) {
    this.setState({
      selectedFile: event.target.files[0],
      fileUrl: URL.createObjectURL(event.target.files[0])
    });
  }

  handleSubmit(event) {
    this.props.onPhotoSubmit(this.state.selectedFile);
    event.preventDefault();
  }

  render() {
    return (
      <div>
        {this.props.children}
        <form onSubmit={this.handleSubmit}>
        <div className="upload">
          <label htmlFor="photo">
            Upload your photo
            <input id="photo" type="file" onChange={this.handleFileChanged} />
          </label>
        </div>
          <img className="photo-prreview" height="200" width="200" src={this.state.fileUrl} />
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}
