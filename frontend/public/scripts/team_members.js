// frontend/public/scripts/team_members.js

const urlParams = new URLSearchParams(window.location.search);
const teamId = urlParams.get("team_id");

function fetchTeamMembers() {
  	fetch(`/api/team_members/${teamId}`)
    	.then(res => res.json())
    	.then(data => {
      		document.getElementById("team-name").textContent = `${data.name}の選手一覧`;
      		const ul = document.getElementById("member-list");
			ul.innerHTML = "";

			data.member_with_profiles.forEach(member => {
                const li = document.createElement("li");

                // メンバー情報を整形して表示
                li.innerHTML = `
                    <strong>${member.name}</strong>
                    （${member.height_cm || "?"}cm / ${member.weight_kg || "?"}kg）
                    <ul>
                        ${member.member_profiles.map(profile => `
                            <li>背番号:${profile.uniform_number || "-"} / 役割:${profile.role || "-"} (from:${profile.since_date || "-"} / ${profile.until_date ? `to ${profile.until_date}` : "active"}</li>
                        `).join("")}
                    </ul>
                `;

                ul.appendChild(li);
            });
		});
}

// function deleteTeamMember(memberId) {
//   fetch(`/api/members/${memberId}`, { method: "DELETE" })
//     .then(() => fetchTeamMembers());
// }

// document.getElementById("add-member-form").addEventListener("submit", function (e) {
//   e.preventDefault();
//   const formData = new FormData(this);
//   formData.append("team_id", teamId);

//   fetch("/api/members", {
//     method: "POST",
//     body: formData
//   }).then(() => {
//     this.reset();
//     fetchTeamMembers();
//   });
// });

function getTodayFormatted() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // 2桁
    const day = String(now.getDate()).padStart(2, '0');        // 2桁
    return `${year}-${month}-${day}`;
}

fetchTeamMembers();
