import SideNav, {Toggle, NavItem, NavIcon, NavText} from '@trendmicro/react-sidenav';
import "@trendmicro/react-sidenav/dist/react-sidenav.css";
import { useNavigate } from 'react-router-dom';

function SideBar(){
    const navigate = useNavigate();
    return <SideNav
        onSelect={selected=> {
            console.log(selected);
            navigate('/'+selected);
        }}
        className='sidebar'>
            <SideNav.Toggle />
            <SideNav.Nav defaultSelected="home">
                <NavItem eventKey="home">
                    <NavIcon><i className='fa fa-fw fa-home' style={{fontSize: 1.5}}></i></NavIcon>
                    <NavText>Home</NavText>
                </NavItem>
                <NavItem eventKey="tutorial">
                    <NavIcon><i className='fa fa-fw fa-home' style={{fontSize: 1.5}}></i></NavIcon>
                    <NavText>Tutorial</NavText>
                </NavItem>
                <NavItem eventKey="about">
                    <NavIcon><i className='fa fa-fw fa-home' style={{fontSize: 1.5}}></i></NavIcon>
                    <NavText>About</NavText>
                </NavItem>
            </SideNav.Nav>
        </SideNav>
}

export default SideBar;