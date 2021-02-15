function SignUpLink({ scrape }) {
    const Button = MaterialUI.Button;

    return (
        <Button
            className="btn"
            variant="contained"
            color="primary"
            href={scrape.url}
            rel="noreferrer"
            target="_blank"
        >
            {scrape.available ? (scrape.walk_in ? "Website" : "Sign Up") : "Website"}
        </Button>
    );
}
