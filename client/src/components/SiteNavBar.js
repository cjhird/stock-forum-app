// Import Link
import { useNavigate, Link } from 'react-router-dom'

// Import React Bootstrap Components
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Container from 'react-bootstrap/Container'
import { Button } from 'react-bootstrap'

import { getTokenFromLocalStorage, userIsAuthenticated } from '../helpers/auth'

const SiteNavBar = () => {
  const navigate = useNavigate()

  // Remove the token from localstorage the button logout is pressed
  const handleLogoutBtn = () => {
    localStorage.removeItem('stock-forum')
    navigate('/')
  }

  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Container as="section" className="nav justify-content-center">
        {/* Navbar brand */}
        {/* Wherever you use a href on a bootstrap component, replace it with an as={Link} and a to="/pathname" */}
        <Navbar.Brand as={Link} to="/">
          STOCK FORUM
        </Navbar.Brand>
        {/* Navbar Toggle is our mobile burger icon - this is displayed at a breakpoint specified on the Navbar component above */}
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        {/* Navbar collapse is our menu wrapped in a collapsible container for mobile */}
        <Navbar.Collapse id="basic-navbar-nav" className="">
          {/* Nav Link is an individual link inside a nav. Same as Nav Brand, to use Link add as={Link} and to="/pathname" */}
          <Nav.Link as={Link} to="/threads">
            Threads
          </Nav.Link>
          {!userIsAuthenticated() ? (
            <>
              <Nav.Link as={Link} to="/register" className="ms-5">
                <Button variant="light">Register</Button>
              </Nav.Link>
              <Nav.Link as={Link} to="/login">
                <Button variant="primary">Login</Button>
              </Nav.Link>
            </>
          ) : (
            <>
              <Nav.Link as={Link} to="/threads/add">
                <Button variant="success">Add +</Button>
              </Nav.Link>
              <Nav.Link onClick={handleLogoutBtn} className="logout-btn">
                <Button variant="primary">Logout</Button>
              </Nav.Link>
            </>
          )}
        </Navbar.Collapse>
      </Container>
    </Navbar>
  )
}

export default SiteNavBar
