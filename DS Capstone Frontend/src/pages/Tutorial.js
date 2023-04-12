import App from "../App"
function Tutorial(){
    return <div className='page' style={{
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
							Tutorial  
						</h1>
            <p style={{color: 'white'}}>
            <b>In this page you will learn how to use the X-ray Image Analysis app</b>
            </p>
            <img src={require('./res/example.jpeg')} alt="example"/>
            <p style={{color: 'white'}}>
            <br/><br/><br/>Step 1: Have ready a valid x-ray image file 
            <br/>(image files supported: .jpg, .jpeg, .png, .bmp, .sr, .tiff, .pbm)
            <br/>
            </p>
            <img src={require('./res/example_xrays.jpeg')} alt="x-ray examples" />
            <p style={{color: 'white'}}>
            *Examples of how the x-ray image should look like
            <br/><br/><br/><br/>Step 2: To upload your x-ray image, click “UPLOAD” button
            <br/>and find the desired x-ray you want evaluate in your computer
            </p>
            <img src={require('./res/example_upload.jpeg')} alt="x-ray examples" />
            <p style={{color: 'white'}}>
            <br/><br/><br/>Step 3: Once uploaded, click on the “Generate” button and wait a 
            <br/>moment for app to process the x-ray's heat map and label
            </p>
            <img src={require('./res/example_gen.jpeg')} alt="x-ray examples" />
            <p style={{color: 'white'}}>
            <br/><br/><br/>Step 4: After a few moments, the app will output the 
            <br/>diagnosis and the heat map of the image
            </p>
            <img src={require('./res/example_fin.jpeg')} alt="x-ray examples" />
            </div>
}

export default Tutorial;