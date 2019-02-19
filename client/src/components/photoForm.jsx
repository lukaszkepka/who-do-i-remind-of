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
    const imagePreview = {
      backgroundImage: `url(${this.state.fileUrl})`,
      backgroundSize: "contain",
      backgroundRepeat: "no-repeat",
      backgroundPosition: "center"
    };
    return (
      <div>
        <div className="form-title">Show Us Your Face</div>
        {this.props.children}
        <form onSubmit={this.handleSubmit}>
          <div class="upload-btn-wrapper" style={imagePreview}>
            <button class="btn">
              {this.state.fileUrl == "" && (
                <>
                  <div>&#8682;</div>
                  <div>Click to Upload</div>
                </>
              )}
            </button>
            <input
              type="file"
              name="myfile"
              onChange={this.handleFileChanged}
            />
          </div>
          {/* <div className="upload">
            <label htmlFor="photo">
              Upload your photo
              <input id="photo" type="file" onChange={this.handleFileChanged} />
            </label>
          </div> */}
          <input type="submit" value="Show Result" />
        </form>
      </div>
    );
  }
}
