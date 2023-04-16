import axios from 'axios';
import { Button } from '@mui/material';
import { CircularProgress } from '@material-ui/core';
import React,{Component, Fragment} from 'react';
import { Col, Row } from "reactstrap";
import {Route, useLocation, BrowserRouter as Router, Routes} from 'react-router-dom';
import SideBar from './components/SideBar';
import './App.css'
import Tutorial from './pages/Tutorial';
import About from './pages/About';
import Home from './pages/Home';
class App extends Component {

	state = {
  image_url: "",
	uploaded_image_url: "",
	selectedFile: null,
	loader: false,
	class_prediction: "",
	isHome: true
	};

	onFileChange = event => {
	
	this.setState({ selectedFile: event.target.files[0], uploaded_image_url: URL.createObjectURL(event.target.files[0]), image_url: ""});	
};

clearSelection = () => {
	this.setState({image_url: "", uploaded_image_url: "", selectedFile: null})
}

onFileUpload = () => {
	this.setState({loader: true, uploaded_image_url: "", image_url: ""})
	const formData = new FormData();
	
	formData.append(
		"myFile",
		this.state.selectedFile,
		this.state.selectedFile.name
		);
		
		axios.post("http://localhost:5000/process_image", formData)
		.then(res => {
			this.setState({
				class_prediction: res.data.data[1],
				uploaded_image_url: URL.createObjectURL(this.state.selectedFile)
				// loader: false
			});
			setTimeout(() => {this.setState({image_url: res.data.data[0], loader: false})}, 3000);
		})
    .catch(err => console.log(err));
	};
	
	
	fileData = () => {
		
		if (this.state.selectedFile) {
			
			return (
				<div>
			<h2 style={{color: 'white'}}>File Details:</h2>
			<p style={{color: 'white'}}>File Name: {this.state.selectedFile.name}</p>
		</div>
		);
	} else {
		return (
			<div>
			<br />
			<h4 style={{color: "white"}}>Click UPLOAD to choose and upload image from device</h4>
		</div>
		);
	}
};

render() {
	let path = "home";
	let pathHome = true, needsReload = true;
	const getPath = () => {
		path = window.location.href;
		path = path.substring(path.length-4);
		if(!path.localeCompare("home")){
			pathHome = true;
			if(!needsReload){
				needsReload = true;
			}
		}
		else{
			pathHome = false;
			if(needsReload){
				this.forceUpdate();
				needsReload = false;
			}
		}
	}
 	return (
		<Router>
			<SideBar/>
			<Routes>
				<Route path='/home' element={Home.render} />
				<Route path='/tutorial' element={<Tutorial/>} />
				<Route path='/about' element={<About/>} />
			</Routes>
			
			{getPath()}
			{pathHome && <div style={{
					overflowY:"auto",
					textAlign: "center",
					backgroundImage: "url(" + "https://t3.ftcdn.net/jpg/01/83/50/32/360_F_183503230_heDoLySnwt4W968RVTJOf7LFHbkZdCHA.jpg" + ")",
					backgroundPosition: 'center',
					backgroundSize: 'cover',
					width:"100%",
					height:"100vh",    
					// overflow:"hidden",
					backgroundRepeat: 'repeat'}}>
						<h1 style={{color: 'white'}}>
							X-Ray Image Analysis
						</h1>
						<div>
							<Button variant="contained" component="label">
								Upload
								<input hidden accept="image/*" type="file" onChange={this.onFileChange}/>
							</Button>				
					{/* <input type="file" onChange={this.onFileChange} /> */}
							<button style={{marginLeft: "50px"}} onClick={!this.state.image_url ? this.onFileUpload: this.clearSelection}>
								{this.state.image_url ? "Clear" : "Generate"}
							</button>
								{this.state.loader && 
								// <LinearProgress/>
								<Fragment>
									<div style={{overflow: "hidden", textAlign:"center", display: "flex", alignItems: "center", justifyContent: "center"}}>
										<CircularProgress style={{marginTop: "20px"}}/>
									</div>
								<div/>
								</Fragment>
								}	
					</div>
					{this.state.uploaded_image_url && !this.state.loader && !this.state.image_url && <img style={{marginTop: "20px", width: "300px", height: "300px"}}src={this.state.uploaded_image_url}/>}
					{this.state.image_url && 
					<Fragment>
						<Row>
							<Col md="6">
								<img style={{marginTop: "20px", width: "200px", height: "200px"}}src={this.state.uploaded_image_url}/>
							</Col>
							<Col md='6'>
								<h2 style={{color: "white"}}>{this.state.class_prediction}</h2>
								<img style={{width: "300px", height: "300px"}}src={"http://localhost:5000/process_image/"+ this.state.image_url }/>
							</Col>
						</Row>
					</Fragment>
					}
				{this.fileData()}
				</div>}
			</Router>
		);
		}
	}

export default App;
