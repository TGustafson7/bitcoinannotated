export async function onRequestPost({ request, env }) {
  try {
    let email = '';
    const ct = request.headers.get('content-type') || '';
    if (ct.includes('application/json')) {
      const body = await request.json();
      email = (body.email || '').trim();
    } else {
      const form = await request.formData();
      email = (form.get('email') || '').toString().trim();
    }

    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      return Response.json({ ok: false, error: 'Please enter a valid email.' }, { status: 400 });
    }

    const res = await fetch('https://api.buttondown.com/v1/subscribers', {
      method: 'POST',
      headers: {
        'Authorization': 'Token ' + env.BUTTONDOWN_API_KEY,
        'Content-Type': 'application/json',
        'X-Buttondown-Bypass-Firewall': 'true',
      },
      body: JSON.stringify({ email_address: email, type: 'regular' }),
    });

    if (res.ok) return Response.json({ ok: true });

    const text = await res.text();
    if (res.status === 400 && /already|exists/i.test(text)) {
      return Response.json({ ok: true, already: true });
    }
    return Response.json({ ok: false, error: 'Subscription failed. Try again.' }, { status: 502 });
  } catch (e) {
    return Response.json({ ok: false, error: 'Server error.' }, { status: 500 });
  }
}
