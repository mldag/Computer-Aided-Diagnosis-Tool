function About(){
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
							About  
						</h1>
        <br/>
        <p style={{color: 'white', fontSize: 27}}>
        <b>Developed by</b>
        </p>
        <img src={require('./res/KFSCIS-hrz-white-gold-logo.png')} alt="example"/>
        <br/><br/><br/>
        <p style={{color: 'white', fontSize: 27}}>
        <b>Powered by</b>
        </p>
        <img src={require('./res/logos.png')} alt="example"/>
        </div>
}

export default About;