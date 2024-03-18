import Button from 'react-bootstrap/Button';
import { CLIENT_ID, SERVER_URL } from '../../constants';
import './Dashboard.scss';

function Dashboard() {
  const stravaLoginUrl = `https://www.strava.com/oauth/authorize?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${SERVER_URL}&approval_prompt=force&scope=activity:read_all`;

  return (
    <div className="main">
      <Button className="login-button" href={stravaLoginUrl} variant="primary" size="lg">
        Login with Strava
      </Button>
    </div>
  );
}

export default Dashboard;
